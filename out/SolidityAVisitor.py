# Generated from ../SolidityA.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SolidityAParser import SolidityAParser
else:
    from SolidityAParser import SolidityAParser

# This class defines a complete generic visitor for a parse tree produced by SolidityAParser.

class SolidityAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SolidityAParser#sourceUnit.
    def visitSourceUnit(self, ctx:SolidityAParser.SourceUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#pragmaDirective.
    def visitPragmaDirective(self, ctx:SolidityAParser.PragmaDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#pragmaName.
    def visitPragmaName(self, ctx:SolidityAParser.PragmaNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#pragmaValue.
    def visitPragmaValue(self, ctx:SolidityAParser.PragmaValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#version.
    def visitVersion(self, ctx:SolidityAParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#versionOperator.
    def visitVersionOperator(self, ctx:SolidityAParser.VersionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#versionConstraint.
    def visitVersionConstraint(self, ctx:SolidityAParser.VersionConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#importDeclaration.
    def visitImportDeclaration(self, ctx:SolidityAParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#importDirective.
    def visitImportDirective(self, ctx:SolidityAParser.ImportDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#importPath.
    def visitImportPath(self, ctx:SolidityAParser.ImportPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#contractDefinition.
    def visitContractDefinition(self, ctx:SolidityAParser.ContractDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#inheritanceSpecifier.
    def visitInheritanceSpecifier(self, ctx:SolidityAParser.InheritanceSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#contractPart.
    def visitContractPart(self, ctx:SolidityAParser.ContractPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#stateVariableDeclaration.
    def visitStateVariableDeclaration(self, ctx:SolidityAParser.StateVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#fileLevelConstant.
    def visitFileLevelConstant(self, ctx:SolidityAParser.FileLevelConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#customErrorDefinition.
    def visitCustomErrorDefinition(self, ctx:SolidityAParser.CustomErrorDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#typeDefinition.
    def visitTypeDefinition(self, ctx:SolidityAParser.TypeDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#usingForDeclaration.
    def visitUsingForDeclaration(self, ctx:SolidityAParser.UsingForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#usingForObject.
    def visitUsingForObject(self, ctx:SolidityAParser.UsingForObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#usingForObjectDirective.
    def visitUsingForObjectDirective(self, ctx:SolidityAParser.UsingForObjectDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#userDefinableOperators.
    def visitUserDefinableOperators(self, ctx:SolidityAParser.UserDefinableOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#structDefinition.
    def visitStructDefinition(self, ctx:SolidityAParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#modifierDefinition.
    def visitModifierDefinition(self, ctx:SolidityAParser.ModifierDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#modifierInvocation.
    def visitModifierInvocation(self, ctx:SolidityAParser.ModifierInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:SolidityAParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionDescriptor.
    def visitFunctionDescriptor(self, ctx:SolidityAParser.FunctionDescriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#returnParameters.
    def visitReturnParameters(self, ctx:SolidityAParser.ReturnParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#modifierList.
    def visitModifierList(self, ctx:SolidityAParser.ModifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#eventDefinition.
    def visitEventDefinition(self, ctx:SolidityAParser.EventDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#enumValue.
    def visitEnumValue(self, ctx:SolidityAParser.EnumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#enumDefinition.
    def visitEnumDefinition(self, ctx:SolidityAParser.EnumDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#parameterList.
    def visitParameterList(self, ctx:SolidityAParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#parameter.
    def visitParameter(self, ctx:SolidityAParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#eventParameterList.
    def visitEventParameterList(self, ctx:SolidityAParser.EventParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#eventParameter.
    def visitEventParameter(self, ctx:SolidityAParser.EventParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionTypeParameterList.
    def visitFunctionTypeParameterList(self, ctx:SolidityAParser.FunctionTypeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionTypeParameter.
    def visitFunctionTypeParameter(self, ctx:SolidityAParser.FunctionTypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SolidityAParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#typeName.
    def visitTypeName(self, ctx:SolidityAParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#userDefinedTypeName.
    def visitUserDefinedTypeName(self, ctx:SolidityAParser.UserDefinedTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#mappingKey.
    def visitMappingKey(self, ctx:SolidityAParser.MappingKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#mapping.
    def visitMapping(self, ctx:SolidityAParser.MappingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#mappingKeyName.
    def visitMappingKeyName(self, ctx:SolidityAParser.MappingKeyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#mappingValueName.
    def visitMappingValueName(self, ctx:SolidityAParser.MappingValueNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionTypeName.
    def visitFunctionTypeName(self, ctx:SolidityAParser.FunctionTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#storageLocation.
    def visitStorageLocation(self, ctx:SolidityAParser.StorageLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#stateMutability.
    def visitStateMutability(self, ctx:SolidityAParser.StateMutabilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#block.
    def visitBlock(self, ctx:SolidityAParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#statement.
    def visitStatement(self, ctx:SolidityAParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#expressionStatement.
    def visitExpressionStatement(self, ctx:SolidityAParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#ifStatement.
    def visitIfStatement(self, ctx:SolidityAParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#tryStatement.
    def visitTryStatement(self, ctx:SolidityAParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#catchClause.
    def visitCatchClause(self, ctx:SolidityAParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#whileStatement.
    def visitWhileStatement(self, ctx:SolidityAParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#simpleStatement.
    def visitSimpleStatement(self, ctx:SolidityAParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#uncheckedStatement.
    def visitUncheckedStatement(self, ctx:SolidityAParser.UncheckedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#forStatement.
    def visitForStatement(self, ctx:SolidityAParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#inlineAssemblyStatement.
    def visitInlineAssemblyStatement(self, ctx:SolidityAParser.InlineAssemblyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#inlineAssemblyStatementFlag.
    def visitInlineAssemblyStatementFlag(self, ctx:SolidityAParser.InlineAssemblyStatementFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:SolidityAParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#continueStatement.
    def visitContinueStatement(self, ctx:SolidityAParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#breakStatement.
    def visitBreakStatement(self, ctx:SolidityAParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#returnStatement.
    def visitReturnStatement(self, ctx:SolidityAParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#throwStatement.
    def visitThrowStatement(self, ctx:SolidityAParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#emitStatement.
    def visitEmitStatement(self, ctx:SolidityAParser.EmitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#revertStatement.
    def visitRevertStatement(self, ctx:SolidityAParser.RevertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#variableDeclarationStatement.
    def visitVariableDeclarationStatement(self, ctx:SolidityAParser.VariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:SolidityAParser.VariableDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#identifierList.
    def visitIdentifierList(self, ctx:SolidityAParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#elementaryTypeName.
    def visitElementaryTypeName(self, ctx:SolidityAParser.ElementaryTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#expression.
    def visitExpression(self, ctx:SolidityAParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:SolidityAParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#expressionList.
    def visitExpressionList(self, ctx:SolidityAParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#nameValueList.
    def visitNameValueList(self, ctx:SolidityAParser.NameValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#nameValue.
    def visitNameValue(self, ctx:SolidityAParser.NameValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionCallArguments.
    def visitFunctionCallArguments(self, ctx:SolidityAParser.FunctionCallArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#functionCall.
    def visitFunctionCall(self, ctx:SolidityAParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyBlock.
    def visitAssemblyBlock(self, ctx:SolidityAParser.AssemblyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyItem.
    def visitAssemblyItem(self, ctx:SolidityAParser.AssemblyItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyExpression.
    def visitAssemblyExpression(self, ctx:SolidityAParser.AssemblyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyMember.
    def visitAssemblyMember(self, ctx:SolidityAParser.AssemblyMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyCall.
    def visitAssemblyCall(self, ctx:SolidityAParser.AssemblyCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyLocalDefinition.
    def visitAssemblyLocalDefinition(self, ctx:SolidityAParser.AssemblyLocalDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyAssignment.
    def visitAssemblyAssignment(self, ctx:SolidityAParser.AssemblyAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyIdentifierOrList.
    def visitAssemblyIdentifierOrList(self, ctx:SolidityAParser.AssemblyIdentifierOrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyIdentifierList.
    def visitAssemblyIdentifierList(self, ctx:SolidityAParser.AssemblyIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyStackAssignment.
    def visitAssemblyStackAssignment(self, ctx:SolidityAParser.AssemblyStackAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#labelDefinition.
    def visitLabelDefinition(self, ctx:SolidityAParser.LabelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblySwitch.
    def visitAssemblySwitch(self, ctx:SolidityAParser.AssemblySwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyCase.
    def visitAssemblyCase(self, ctx:SolidityAParser.AssemblyCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyFunctionDefinition.
    def visitAssemblyFunctionDefinition(self, ctx:SolidityAParser.AssemblyFunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyFunctionReturns.
    def visitAssemblyFunctionReturns(self, ctx:SolidityAParser.AssemblyFunctionReturnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyFor.
    def visitAssemblyFor(self, ctx:SolidityAParser.AssemblyForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyIf.
    def visitAssemblyIf(self, ctx:SolidityAParser.AssemblyIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#assemblyLiteral.
    def visitAssemblyLiteral(self, ctx:SolidityAParser.AssemblyLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#tupleExpression.
    def visitTupleExpression(self, ctx:SolidityAParser.TupleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#numberLiteral.
    def visitNumberLiteral(self, ctx:SolidityAParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#identifier.
    def visitIdentifier(self, ctx:SolidityAParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#hexLiteral.
    def visitHexLiteral(self, ctx:SolidityAParser.HexLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#overrideSpecifier.
    def visitOverrideSpecifier(self, ctx:SolidityAParser.OverrideSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityAParser#stringLiteral.
    def visitStringLiteral(self, ctx:SolidityAParser.StringLiteralContext):
        return self.visitChildren(ctx)



del SolidityAParser